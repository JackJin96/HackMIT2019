from App.micStream import MicrophoneStream

from rev_ai.models import MediaConfig
from rev_ai.streamingclient import RevAiStreamingClient

import flask
import json

def executeStreaming(socketio):
    # Sampling rate of your microphone and desired chunk size
    rate = 44100
    chunk = int(rate/10)

    # Insert your access token here
    access_token = "02_qnlgLZ05eoZPxN89yiouX3gTB86Dsw1uHIlgjSRbKt536KESupmymFaQOYTEMBi1_nR28sgGlSVyidxCBjGzYVLgNk"

    # Creates a media config with the settings set for a raw microphone input
    example_mc = MediaConfig('audio/x-raw', 'interleaved', 44100, 'S16LE', 1)

    streamclient = RevAiStreamingClient(access_token, example_mc)

    # Opens microphone input. The input will stop after a keyboard interrupt.
    with MicrophoneStream(rate, chunk) as stream:
        # Uses try method to allow users to manually close the stream
        try:
            # Starts the server connection and thread sending microphone audio
            response_gen = streamclient.start(stream.generator())

            # Iterates through responses and prints them
            elements=""
            resp=""
            for response in response_gen:
                print(response)
                resp=json.loads(response)

                # if (resp["type"]=="final"):
                #     elements=resp["elements"]
                elements=resp["elements"]
                txt=""
                for val in elements:
                    #print(val["value"])
                    if(val["type"]=="punct"):
                        txt=txt+val["value"]
                    else:
                        txt=txt+" "+val["value"]
                    #print(txt)

                socketio.emit('my data', {
                    'content': txt,
                    'type': resp["type"],
                })

                #print(txt);

        except KeyboardInterrupt:
            # Ends the websocket connection.
            streamclient.client.send("EOS")
            pass
