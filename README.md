# ELeNA : Elevation based Navigation

## ELeNA
Elevation-based Navigation (EleNa) is a map based application that gives the user a preferred route between any two points on the map that either minimizes or maximizes the elevation gain and is within “x%” of the shortest path possible where x is user specified.

## Web Application
* The web application follows the client-server architecture. 
* The frontend of the application is built on ReactJs and is rendered at `http://localhost:3000`.
![alt text](./images/img1.png)
* The web server (backend) for the application is built on Python (majorly Flask) and is served at `http://localhost:5000`.

![alt text](./images/img5.png)

* We have followed MVC architecture for building the backend of the application.

* Path rendered when `No Elevation` is selected.
![alt text](./images/img2.png)

* Path rendered when `Min Elevation` is selected with 50% of the shortest path.
![alt text](./images/img3.png)

* Path rendered when `Max Elevation` is selected with 50% of the shortest path.
![alt text](./images/img4.png)

## How to Run

### Frontend Application
* Ensure the system has node, npm installed.
* Move to the project's frontend directory.<br>
`cd ./src/client/`
* Install the required dependencies.<br>
`npm install`
* Run the react web app.<br>
`npm start`

### Backend Application
* Ensure python is installed on the system, and the python version is >=3.10
* Move to the project's backend directory.<br>
`cd ./src/server/src`
* (Optional) Instead of installing the packages on the system, we can make a virtual environment and install the packages.<br>
`python -m venv virtual_env`
* Enter the virtual environment.<br>
`source virtual_env/bin/activate`
* Install the required packages.<br>
`pip install -r requirements.txt`
* Run the flask server.<br>
`python app.py`


### Testing 
#### Frontend Testing

* Move to the project's frontend directory.<br>
`cd ./src/client/`

* Run the following commands to run jest tests.<br>
`npm test`<br>
> Enter a to run all the tests.

![alt text](./images/img6.png)

#### Backend Testing

* Move to the project's backend directory.<br>
`cd ./src/server/src`

* Run the following commands to run junit tests.<br>
`python3 -m unittest test.test`

![alt text](./images/img7.png)

