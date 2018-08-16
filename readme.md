# data visualizations

## Jupyter notebooks
Various data visualization projects. View them all [here](http://nbviewer.jupyter.org/github/markmisener/data-visualization/tree/master/).

### 911 calls in Seattle, WA

Using the `sodapy` python client for the Socrata Open Data API and [Mapboxgl-jupyter](https://github.com/mapbox/mapboxgl-jupyter), check out 911 calls in Seattle, WA in real time. View the notebook [here](http://nbviewer.jupyter.org/github/markmisener/data-visualization/blob/master/mapboxgl-jupyter/911%20Calls%20in%20Seattle%2C%20WA.ipynb).

<img width="949" alt="screen shot 2018-08-15 at 5 29 58 pm" src="https://user-images.githubusercontent.com/11286381/44180396-fdf23f80-a0b0-11e8-9b0e-805827a68cf2.png">

### Alameda County Sherriff crime reports


Using the `sodapy` python client for the Socrata Open Data API and [Mapboxgl-jupyter](https://github.com/mapbox/mapboxgl-jupyter), check out Alameda County Sheriff Crime Reports from January 1, 2012 to present. View the notebook [here](http://nbviewer.jupyter.org/github/markmisener/data-visualization/blob/master/mapboxgl-jupyter/Alameda%20County%20Sheriff%20Crime%20Reports.ipynb).


<img width="957" alt="screen shot 2018-08-15 at 5 30 33 pm" src="https://user-images.githubusercontent.com/11286381/44180398-fe8ad600-a0b0-11e8-9c5d-9bd606918172.png">

### Divvy bike share availability

Using a feed of data made available by [Motivateco](https://www.motivateco.com/) and [Mapboxgl-jupyter](https://github.com/mapbox/mapboxgl-jupyter), we can visulize which bike docks in Chicago currently have available bikes.

<img width="954" alt="screen shot 2018-08-15 at 5 30 46 pm" src="https://user-images.githubusercontent.com/11286381/44180397-fe8ad600-a0b0-11e8-8980-e03b7f41210c.png">


## Flask dashboard
A work in progress Flask dashboard of various data visualizations.

### Serve locally
``` sh
git clone git@github.com:markmisener/data-visualization.git
cd data-visualization/dashboard
pip install -r requirements.txt
python app.py
```

### US Population Density by State

<img width="1421" alt="screen shot 2018-08-15 at 5 30 07 pm" src="https://user-images.githubusercontent.com/11286381/44180395-fdf23f80-a0b0-11e8-957c-23ed2336abde.png">


After running the commands above to serve the dashboard, visit http://127.0.0.1:5000/ to view US Population Density by State.
