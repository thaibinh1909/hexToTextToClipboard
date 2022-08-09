import subprocess

vEncode = "utf-8"
vWinClipboard = "clip.exe"
  
vInputText = "Enter to exit or paste HEX below:\n"
vOutputText = "\nBelow result has been in your clipboard already.\nResult:"
vErrMsg = "Not a HEX string, retry!"  

while True:  

    vInput = input(vInputText)
    
    if vInput == "":
        break

    try:
        vOutput = bytes.fromhex(vInput).decode(vEncode)
    except ValueError:
        print(vErrMsg)
        continue
    
    subprocess.run([vWinClipboard], input=vOutput.strip().encode(vEncode), check=True)
    print(vOutputText, vOutput, "\n")