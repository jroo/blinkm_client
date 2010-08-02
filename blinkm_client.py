import blinkm_serial, simplejson, time, urllib

INSTRUCTION_URL = ""
BLINKM_PORT = ""
 
def call_method(method, arguments):
    function = getattr(b, method)
    return function(**arguments)

def get_instruction(instruction_url):    
    instruction = simplejson.load(urllib.urlopen(INSTRUCTION_URL))
    return { "id":instruction['instruction_id'], "payload": {"method":instruction['method'], "arguments":instruction['arguments'] } }

last_instruction = None
b = blinkm_serial.BlinkMSerial(BLINKM_PORT)
while True:
    try:
        instruction = get_instruction(INSTRUCTION_URL)
    except:
        pass

    if instruction['id'] <> last_instruction:
        try:
            b.open()
            call_method(**instruction['payload'])
            b.close()
            last_instruction = instruction['id']
        except:
            pass

    time.sleep(2)