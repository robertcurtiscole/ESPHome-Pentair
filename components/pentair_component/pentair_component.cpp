#include "esphome/core/log.h"
#include "pentair_component.h"

namespace esphome {
namespace pentair_component {

static const char *TAG = "pentair_component";

void PentairRS422::setup() {
      // nothing to do here
    ESP_LOGI(TAG, "PentairRS422 setup().");
   
    loop_count_ = 0;
    // else if any failure
    // this->mark_failed();
    // return;
    ESP_LOGE(TAG, "Setup completed.");    
}
  
void PentairRS422::loop() {
     // junk debug
    if ((++loop_count_ %300) == 0) {
        if (this->water_temp_sensor_) {
            this->water_temp_sensor_->publish_state(random_float() * 50);
        }
       if (this->spa_on_switch_) {
            this->spa_on_switch_->publish_state(random_uint32()%2);
        }
    }

    // This will be called by App.loop()
    boolean got_char = false;
    char msgbuffer[40];
    while (available()) {
        loop_chars++;     // count loops with char
        got_char = true;
        int c = read();
        addchar(c);

        // check for valid start chars, discard all others
        if (nchars >= 1 && nchars <= 4 && buffer[nchars-1] != starthead[nchars-1])
        {
            resetBuffer();    // wrong start, ignore
        }

        // Did we get the msg length?
        if (nchars == 8) {
            msglen = buffer[7];
        }

        // did we get the checksum?  msglen plus 8 plus 2
        if (nchars == msglen + 10) {
            if (checksumPass(buffer, nchars)) {
                // id(debug_text).publish_state("Checksum Passed");

                // is this the right message?
                // check source/destination (0x10, 0x0f) and station update command (0x02)
                if (buffer[4] == 0x0F && buffer[5] == 0x10 && buffer[6] == 0x02) {

                    // spa on?
                    /*****
                    curSpaHeater = (bool) (buffer[8+2] & 0x01);
                    if (curSpaHeater != cmdSpaHeater) {
                        if (curSpaHeater != (bool)( id(spaheater).state)) {
                            id(spaheater).toggle();      // set switch to current state
                        }
                    }
                    *****/
    
                    // spa and pool temperatures +14, +15
                    if (this->water_temp_sensor_) {
                        sprintf(msgbuffer, "%d°F ", (int) buffer[8+14]);
                        this->water_temp_sensor_->publish_state(msgbuffer);
                    }
                    if (this->spa_temp_sensor_) {
                        sprintf(msgbuffer, "%d°F ", (int) buffer[8+15]);
                        this->spa_temp_sensor_->publish_state(msgbuffer);
                    }
                    if (this->air_temp_sensor_) {
                        sprintf(msgbuffer, "%d°F ", (int) buffer[8+18]);
                        this->air_temp_sensor_->publish_state(msgbuffer);
                    }
                    if (this->solar_temp_sensor_) {
                        sprintf(msgbuffer, "%d°F ", (int) buffer[8+18]);
                        this->solar_temp_sensor_->publish_state(msgbuffer);
                    }

                    // debug strings
                    sprintf(msgbuffer, "Circuits 0x%02X%02X Loops %d/%d", buffer[8+2], buffer[8+3], loop_chars, loop_nochars);
                    //id(debug_text).publish_state(msgbuffer);
                }
            }
            else {
                // id(debug_text).publish_state("Checksum Failed");
            }
            resetBuffer();
            loop_chars = 0;   // reset for next message.
            loop_nochars = 0;
        }
    }

    // count loops without data, idle comms
    if (!got_char) {
        loop_nochars++;
    }
    // no chars to read.
    // if we're not in the middle of a message and we've got something to send, do it now (wait for idle comms)
    if (nchars == 0 && loop_nochars > 30) {
        // if something to send, package it up
        /****
        if (curSpaHeater != (bool) id(spaheater).state) {
            // have we not-yet sent our command?
            if (cmdSpaHeater != (bool) id(spaheater).state) {
                // send the command
                cmdSpaHeater = (bool) id(spaheater).state;
                sprintf(msgbuffer, "Send Heater Cmd %s", cmdSpaHeater? "On-1`" : "Off-0");
                //id(debug_text).publish_state(msgbuffer);
                sendCircuitChange(0x01 ,cmdSpaHeater);
            }
        }
        ****/
    }
}


// circuit status change request message, outgoing
/*
* https://docs.google.com/document/d/1M0KMfXfvbszKeqzu6MUF_7yM6KDHk8cZ5nrH1_OUcAc/edit?tab=t.0
*
* This message is sent by the QuickTouch remote control transceiver to effect a circuit state change.
* The first byte of the data is the circuit number. This is not byte [2] of status message! Rather, it is one of
* these codes: 0x01 represents the SPA, 0x02 is AUX1, 0x03 is AUX2, 0x04 is AUX3, and 0x05 is FEATURE1, 0x06 is POOL,
* 0x07 is FEATURE2, 0x08 is FEATURE3, 0x09 is FEATURE4, 0x85 is HEAT_BOOST.
* The second byte of the data  represents the desired state of the circuit, 0x01 for on, 0x00 for off.
* So, for example, this command would turn the spa on:
* <---HEADER---> PROT   DST  SRC    CMD   DLEN <--DATA->   CHECKSUM
* 0x00 0xFF 0xA5 0x01   0x10 0x48   0x86  0x02 0x01 0x01   0x01 0x88
* ack rcvd:
* 0x00 0xFF 0xA5 0x01   0x48 0x10   0x01  0x01 0x86        0x01 0x88 (or some checksum)
* The message needs a prelude of some # of 0xFF before the header.  Try 8 and send bytes quickly...
*/
void PentairRS422::sendCircuitChange(char circuit, bool state){
    u_char out_message[12] = { 0x00, 0xFF, 0xA5, 0x01, 0x10, 0x20, 0x86, 0x02,
                            0x00, 0x00, 0x00, 0x00};   // set these: data and checksum
    u_char prelude[8] = { 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF };
    uint16 checksum  = 0;


    // set circuit and value
    out_message[8] = circuit;
    out_message[9] = state ? 1: 0;
    checksum = computeChecksum(out_message);
    out_message[10] = checksum >> 8;
    out_message[11] = checksum & 0xFF;
    // write it
    this->write_array(prelude, sizeof(prelude));
  
    this->write_array(out_message, sizeof(out_message));

    this->flush();       
}

     // compute and compare checksums
uint16 PentairRS422::computeChecksum(u_char *buff) {
    uint16 compSum = 0;
    int    lastChar = buff[7] + 8;    // len in message plus six before (offset by 2)
    for (int i = 2; i < lastChar; i++) {
        compSum += (uint16) buff[i];
    }
    /*
    * char testtext[60];
    * uint16 csum2 = buff[2] + buff[3] + buff[4]+ buff[5] + buff[6] + buff[7] + buff[8] + buff[9];
    * snprintf(testtext,sizeof(testtext),"CK 0x%02X %02X %02X %02X %02X %02X %02X %02X 0x%02X%02X vs 0x%04X vs 0x%04X", buff[2], buff[3], buff[4], buff[5], buff[6], buff[7],
    *                 buff[lastChar-2], buff[lastChar-1], buff[lastChar], buff[lastChar+1], compSum, csum2);
    * id(debug_text).publish_state(testtext);
    */

    return compSum;
}


boolean PentairRS422::checksumPass(u_char *buff, int numchars) {
    uint16 sentSum = 0;
    uint16 compSum = 0;

    sentSum = (((uint16) buff[numchars-2]) << 8) + (uint16) buff[numchars-1];
    compSum = computeChecksum(buff);

    return (sentSum == compSum);
}

void PentairRS422::resetBuffer() {
    nchars = 0;     // flush
    msglen = 0;
}


void PentairRS422::addchar(char c) {
    buffer[nchars++] = c;
    // check overflow
    if (nchars > 200) {
        resetBuffer();
}

void PentairRS422::dump_config() {
    ESP_LOGCONFIG(TAG, "PentairRS422 component");
}

} //namespace pentair_component
} //namespace esphome

