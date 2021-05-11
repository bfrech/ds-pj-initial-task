# DS-PJ Initial Task

OpenWhisk and TinyFaas tasks for PJ-DS 2021.

## OpenWhisk
The openwhisk directory contains the cluster setup and two directories with actions. 

#### Prerequisites
Docker, kubectl installed and openwhisk deployed on Kubernetes cluster (https://github.com/apache/openwhisk-deploy-kube/blob/master/README.md)

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
The trigger action queries the https://api.coindesk.com/v1/bpi/currentprice.json API and returns the current Bitcoin rate in EUR and the current timestamp. To create and invoke the action go to openwhisk/trigger directory and run:
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
To see the last few activations run ``` wsk -i activation list --limit 5```

Get result with ```wsk -i activation result <Activation ID>```

To stop the trigger run ``` wsk -i trigger delete five-mins-trigger ```


## OpenFaas
#### Prerequisites
Docker, kubectl and k3d installed and OpenFaas deployed on Kubernetes cluster. 
OpenFaas gateway:
```bash
    kubectl port-forward svc/gateway -n openfaas 8080:8080
```

#### Public-IP
This function uses https://api.ipify.org/?format=json to get the public IP address.
```bash
    echo "" | faas-cli invoke public-ip
```

#### Location
This function returns the location of a public IP address from https://ipinfo.io/92.212.2.145/geo
```bash
    echo <IP-Address> | faas-cli invoke location
```

#### Where am I?
This function first retrieves the public IP address with the public-ip function and then directly retains the location by calling the location function. 
```bash
    echo "" | faas-cli invoke whereami
```

#### Is there still a curfew?
This function uses https://api.corona-zahlen.org/states/BE/history/incidence/5 to get the corona cases of Berlin during the last 5 days and checks whether the weekly incidence was above 100 on any day.
```bash
    echo "" | faas-cli invoke is-there-still-a-curfew
```
