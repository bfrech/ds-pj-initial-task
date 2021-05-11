# DS-PJ Initial Task

OpenWhisk and TinyFaas tasks for PJ-DS 2021.

## OpenWhisk
The openwhisk directory contains the cluster setup and two directories with actions. 

#### Hash Function
The Hash action takes the parameter course as input and returns the MD5 Hash of the concatenated string *course* + Berit.
In openwhisk/hash-function directory run:
```bash
npm install
zip -r hash-function *
wsk -i action create hash-function --kind nodejs:default hash-function.zip
wsk -i action invoke --result hash-function
wsk -i action invoke --result hash-function --param course DS-PJ
```

#### Trigger Function
The trigger action queries the ... API and returns the ... with the current timestamp. To create and invoke the action go to openwhisk/trigger directory and run:
```bash
npm install
zip -r trigger *
wsk -i action create trigger-action --kind nodejs:default trigger.zip
wsk -i action invoke --result trigger-action
```

This code generates a trigger that fires every 5 minutes and invokes trigger-action through a rule. See https://github.com/apache/openwhisk-package-alarms for the documentation of periodic triggers.

```bash
    wsk -i trigger create five-mins-trigger --feed /whisk.system/alarms/interval --param minutes 5
    wsk -i rule create rule1 five-mins-trigger trigger-action
```
To see the last few activations run: 
```bash
    wsk -i activation list --limit 5
```
Get result with ```wsk -i activation result <Activation ID>```

To stop the trigger run:
```bash
    wsk -i trigger delete five-mins-trigger
```
