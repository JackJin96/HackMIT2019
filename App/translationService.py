from App.micStream import MicrophoneStream

from rev_ai.models import MediaConfig
from rev_ai.streamingclient import RevAiStreamingClient

import flask
import json
import time
import datetime

def executeStreaming(socketio, status):
    # Sampling rate of your microphone and desired chunk size
    rate = 44100
    chunk = int(rate/10)

    # Insert your access token here
    access_token = "02_qnlgLZ05eoZPxN89yiouX3gTB86Dsw1uHIlgjSRbKt536KESupmymFaQOYTEMBi1_nR28sgGlSVyidxCBjGzYVLgNk"

    # Creates a media config with the settings set for a raw microphone input
    example_mc = MediaConfig('audio/x-raw', 'interleaved', 44100, 'S16LE', 1)

    streamclient = RevAiStreamingClient(access_token, example_mc)
    start_time = time.time()

    # Opens microphone input. The input will stop after a keyboard interrupt.
    with MicrophoneStream(rate, chunk) as stream:
        # Uses try method to allow users to manually close the stream
        try:
            # Starts the server connection and thread sending microphone audio
            if status == "open":
                response_gen = streamclient.start(stream.generator())
                # Iterates through responses and prints them
                elements=""
                resp=""
                ct = 0
                for response in response_gen:
                    # print(response)
                    resp=json.loads(response)

                    # if (resp["type"]=="final"):
                    #     elements=resp["elements"]
                    elements=resp["elements"]
                    sentense_type = resp["type"]
                    txt=""
                    if sentense_type == "partial":
                        for val in elements:
                            #print(val["value"])
                            if(val["type"]=="punct"):
                                txt=txt+val["value"]
                            else:
                                txt=txt+val["value"]+" "
                            #print(txt)
                    else:
                        for val in elements:
                            txt=txt+val["value"]
                        ct += 1

                    if(ct==5):
                        ct=0
                        sec = datetime.timedelta(seconds=int(time.time()-start_time))
                        tstamp=datetime.datetime(1,1,1)+sec
                        timestamp="["+str(tstamp.hour)+":"+str(tstamp.minute)+":"+str(tstamp.second)+"]"
                        txt=txt+" "+ str(timestamp)

                    socketio.emit('my data', {
                        'content': txt,
                        'type': resp["type"],
                    })
            else:
                # streamclient.end()
                stream._clear_buffer()

        except KeyboardInterrupt:
            # Ends the websocket connection.
            streamclient.client.send("EOS")
            pass
