# arduino-tp-link-smart-plugs
Control TP-Link smart plugs with arduino and raspberry pi or any other linux system. I only own the TP-Link Smart Wi-Fi Plug Mini HS105, but I think it also works with their other similar smart plugs since you can control most of them with your KASA account.

## Preliminary steps
In order to control the smart plugs, you need to get your TP-Link KASA token from your account, the end point URL for your smart plugs, and the deviceId of them aswell. 

### TP-Link KASA token
Firstly, to get the token from your account, you need to do a POST request to https://wap.tplinkcloud.com like this one:

```
{
  "method": "login",
  "params": {
  "appType": "Kasa_Android",
  "cloudUserName": "XXXXXXX",
  "cloudPassword": "XXXXXXX",
  "terminalUUID": "UUIDv4"
 }
}
```

You will first need to replace the XXXXXXX with you TP-Link KASA account credentials and UUIDv4 to one that you generate, you can generate one [here](http://onlineuuidgenerator.com). To facilitate the POST request, you can use this site [hurl.it]. Under destination, change GET to POST and the destination URL is https://wap.tplinkcloud.com, add a header name called *Content-type* with the value of *application/json*, under parameters, click on add body and copy the block of code above with your information, and click on *Launch Request*. If all went well, you should get a JSON response from the server and your TP-Link Kasa token will be in that data.

### End point URL and deviceId
Secondly, to get the end point URL and the deviceID, you need do another POST request. The location will be https://wap.tplinkcloud.com/?token=ACQUIRED_TOKEN, you just need to change the last part *ACQUIRED_TOKEN* to the TP-Link KASA account token you got in previously. You can follow the same steps mentionned previously, but in the parameters's body, you will need to only put this:

```
{"method":"getDeviceList"}
```

You will get another JSON response from the server. Here what we are looking for if the value of "appServerURL" (which is the end point URL) and all of the values of "deviceId" in the list of "deviceList". In order to identify the device, in the same list element, you will see "alias" which has the name of the smart plug.

Afterwards, you only need to change XXXXXXXXXX in the code with XXXXXXXXXXXXXX. Eventually this process will be a little more automated once I learn more how to do and handle POST requests in Python.
