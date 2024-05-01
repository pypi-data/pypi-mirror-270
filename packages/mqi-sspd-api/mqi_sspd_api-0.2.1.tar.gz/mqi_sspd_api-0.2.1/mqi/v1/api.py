# Copyright 2024 The MQI Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

import websocket 
import rel
import json
import logging

# Configure logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_convert_into_two_lists(json_string):
    try:
        # Parse the JSON string
        data = json.loads(json_string)
        
        # Get the 'body' value, assuming it's a single string of comma-separated numbers
        number_string = data["body"]
        
        # Split the string on commas to get a list of strings
        number_list = number_string.split(',')
        
        # Determine the midpoint of the list
        midpoint = len(number_list) // 2
        
        # Convert the first half to floats and the second half to booleans
        float_values = [float(num) for num in number_list[:midpoint]]
        bool_values = [bool(int(num)) for num in number_list[midpoint:]]
        
        return float_values, bool_values
    except (json.JSONDecodeError, KeyError, ValueError) as e:
        # Handle errors: JSON parsing errors, missing 'body' key, or conversion errors
        logging.error(f"Error: {e}")
        return [], []

def extract_values(json_string):
    try:
        # Parse the JSON string
        data = json.loads(json_string)
        
        # Get the 'body' value, assuming it's a single string of comma-separated numbers
        number_string = data["body"]
        
        # Split the string on commas to get a list of strings
        number_list = number_string.split(',')
        
        # Convert the list of strings to a list of floats
        result = [float(num) for num in number_list]
        
        return result
    except (json.JSONDecodeError, KeyError, ValueError) as e:
        # Handle errors: JSON parsing errors, missing 'body' key, or conversion errors
        logging.error(f"Error: {e}")
        return []
    
def extract_body_value(json_string):
    try:
        # Parse the JSON string
        data = json.loads(json_string)
        
        # Return the value associated with the 'body' key directly
        return int(data["body"])
    except (json.JSONDecodeError, KeyError) as e:
        # Handle JSON parsing errors and missing 'body' key
        logging.error(f"Error: {e}")
        return None

"""MQI is the main entry point of the api used to do most high level tasks"""
class MQI:
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
        self.ws = None
        logging.info("MQI initialized with hostname: %s and port: %s", hostname, port)


    """
    connect will create a connection to the cosen Raspberry Pi websocket. 
    If there is no avaialable a "NotFound" error is returned.

    @returns void

    """
    def connect(self):
        try:
            self.ws = websocket.WebSocket()
            self.ws.connect(f"{self.hostname}:{self.port}")
            response = self.ws.recv()
            logging.info("Connected to WebSocket at %s:%s", self.hostname, self.port)
            logging.debug("Initial response from WebSocket: %s", response)
        except Exception as e:
            logging.error("Failed to connect to WebSocket: %s", e)

    def sendMessage(self, command, arduinoID=0, channel=0, value=0):
        data = {
            "__MESSAGE__": "message",
            "command": command,
            "arduinoID": int(arduinoID),
            "id": int(channel),
            "name": "",
            "value": float(value)
        }
        try:
            self.ws.send(json.dumps(data))
            logging.debug("Sent message: %s", data)
            return True
        except Exception as e:
            logging.error("Error sending message: %s", e)
            return False

    def receiveResult(self):
        try:
            self.ws.recv()  # Skip fake MSG1
            self.ws.recv()  # Skip fake MSG2
            result = self.ws.recv()
            logging.debug("Received result: %s", result)
            return result
        except Exception as e:
            logging.error("Failed to receive result: %s", e)
            return None
    """
    set_current will set the bias of the given arduino channel to the value

    @param arduino_id:int -- id of the arduino (0-4)
    @param channel:int -- channel id, can vary but will probably be in the range 0-7
    @param value:float -- the current value in mA
    @returns bool 

    """
    def setCurrent(self, arduino_id,channel, value ):
        
        self.sendMessage("setCurrent", arduino_id, channel, value)
        if extract_body_value(self.receiveResult())==200:
            logging.info("setCurrent for Arduino=%i Channel=%i, Volt=%f ", arduino_id, channel,value)
            return True
        else:
            logging.error("didnt work to setCurrent for Arduino=%i Channel=%i, Volt=%f ", arduino_id, channel,value)
            return False
    """
    get_bias will return the bias of the channel for the given arduino id

    @param arduino_id:int -- id of the arduino (0-7)
    @param channel:int -- value of the channel, can vary but will be in the range 0-8
    @returns [DAC-Values]

    """
    def getDacBias(self, arduino_id=0):
        self.sendMessage("getBias", arduino_id)

        return extract_values(self.receiveResult())

    """
    get_resolution will return the resolution of the arduino

    @param arduino_id
    @returns JsonObject
    """
    def getResolution(self, arduino_id):
        pass

    """
    getStatus will return the status of the arduino

    @param arduino_id
    @returns    true if everything is ok
                false if something wrong
    """
    def getStatus(self, arduino_id):
        self.sendMessage("status", arduino_id)
        return extract_body_value(self.receiveResult())==200



    """
    getAdcBias will return the bias currents of all channels of the arduino

    @param arduino_id:int -- the id of the arduino to select
    @returns [ADC-Values], [ValidChannels]
    """
    def getAdcBias(self, arduino_id):
        self.sendMessage("allChannels", arduino_id)
        return extract_convert_into_two_lists(self.receiveResult())
    
    """
    numb_of_arduinos will return number of arduinos which connected to Control box
    @returns number of Arduinos
    """
    def getNumbOfArduinos(self, arduino_id):
        self.sendMessage("numb_of_arduinos")
        return extract_body_value(self.receiveResult())
    
    """
    restartArduino restart a arduino. it takes about 5 seconds for the arduino to restart
    @param arduino_id:int -- the id of the arduino to select
    """
    def restartArduino(self, arduino_id):
        self.sendMessage("restartArduino", arduino_id)
        return

    """
    restartRPI restart takes about 30 seconds
    """
    def restartRPI(self):
        self.sendMessage("restartRPI")
        return

    """
    current_sweep will initiate a current sweep for the channel chosen

    @param arduino_id:int -- id of the arduino to select
    @param fr:float -- short for from, this is the current to start from (mA)
    @param to:float -- the current to stop at (mA)
    @param channel:int -- channel to select
    @param step_size:float -- the value to increment by
    @returns bool
    
    """
    def currentSweep(self, arduino_id, fr, to, channel, step_size):
        pass


    """
    current_sweep_full will initiate a current sweep for all channels on the arduino

    @param arduino_id:int -- id of the arduino to select
    @param fr:float -- short for from, this is the current to start from (mA)
    @param to:float -- the current to stop at (mA)
    @param channel:int -- channel to select
    @param step_size:float -- the value to increment by
    @returns bool

    """
    def currentSweepFull(self, arduino_id, fr, to, channel, step_size):
        pass

    """
    get_arduino_info will return the hardware specs of the arduino

    @param arduino_id:int -- id of the arduino to select
    @returns JsonObject
    """
    def getArduinoInfo(self, arduino_id):
        pass

    """
    get_arduino_config will return the current config of the selected arduino

    @param arduino_id:int -- id of the arduino to select
    """
    def getArduinoConfig(self, arduino_id):
        data = {
                "__MESSAGE__": "message",
                "command": "initinfo",
                "id": "",
                "name": "",
                "value": "" 

        }

        self.ws.send(json.dumps(data))
        print(self.ws.recv())

        return True
        pass

    """
    set_arduino_config will set the config for the selected arduino

    @param arduino_id: int -- id of the arduino to select
    @returns bool

    """
    def setArduinoConfig(self, arduino_id):
        pass


    """ 

    auth will authenticate a user

    @param username: string -- this is the username usually just an email
    @param password:string -- a secret password 
    @returns bool

    """
    def auth(self, username, password):
        data = {
                "__MESSAGE__": "message",
                "command": "login",
                "id": username,
                "name": "",
                "value": password

        }

        self.ws.send(json.dumps(data))
        print(self.ws.recv())

        return True

    """
    get_logs will return the logs of the managing_module 

    @param filename:string
    @returns bool

    """
    def getLogs(self, filename):
        pass

    """
    set_channels will update the number of channels for the given arduino

    @param arduino_id:int -- the arduino to update
    @param channel_num:int -- the new number of channels
    @returns bool
    """
    def setChannels(self, channel_num, arduino_id=0):

        data = {
                "__MESSAGE__": "message",
                "command": "setChannels",
                "id": channel,
                "name": "",
                "value": channel_num 

        }

        self.ws.send(json.dumps(data))
        print(self.ws.recv())

        return True

    """

    @returns JsonObject
    """
    def getCurrentWs(self):
        return self.ws;

    """
    get_number_of_arduinos returns the number of arduinos currently connected

    @returns int
    """
    def getNumberOfArduinos(self):
        pass


    """
    get_max_currents returns the switching currents for all channels

    @returns int[]
    """
    def getMaxCurrents(self):
        pass


    """
    get_max_current returns the switching currents for the given arduino
    """
    def getMaxCurrent(self, arduino_id):
        pass


    """
    get_current_sweep returns timeseries of the current sweep

    @param arduino_id:int -- id of the arduino
    """
    def getCurrentSweep(self, arduino_id):
        pass


    """
    get_current_sweep_all 

    @returns int[]
    """
    def getCurrentSweepAll(self):
        pass

