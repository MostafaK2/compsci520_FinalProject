import { MapContainer, TileLayer, Marker, Polyline } from "react-leaflet";
import L from "leaflet";
import "leaflet/dist/leaflet.css";
import icon from "leaflet/dist/images/marker-icon.png";
import iconShadow from "leaflet/dist/images/marker-shadow.png";
import { Container } from "../Store/Provider";
import { useState, useEffect } from "react";
import hash from 'object-hash';

let DefaultIcon = L.icon({
  iconUrl: icon,
  shadowUrl: iconShadow,
});

L.Marker.prototype.options.icon = DefaultIcon;

const get_distance = (from, to)  => {
  let fromLatLng = L.latLng(from);
  let toLatLng = L.latLng(to);

  return fromLatLng.distanceTo(toLatLng);
}

const getLineMarkers = (all_markers) => {
  if(all_markers.length === 0) return [];

  let markers = []
  markers.push(all_markers[0]);

  for (let i = 1; i < all_markers.length-1; i++) {
    const dist = get_distance(all_markers[i], markers[markers.length-1]);
    // console.log(dist);
    if(dist > 500) {
      console.log(dist)
      markers.push(all_markers[i]);
    }
  }
  markers.push(all_markers[all_markers.length-1])

  return markers;
}

export const Map = () => {
  const [zoomLocation, setZoomLocation] = useState([42.3754, -72.5193]);
  const [markers, setMarkers] = useState({ startMarker: [], endMarker: [] });
  const [polyline, setPolyline] = useState([]);
  const [keyValue, setKeyValue] = useState("initial");
  const container = Container.useContainer();

  useEffect(() => {
    setZoomLocation(container.newLocation);
    // console.log(markers);
    let newMarker = markers;
    newMarker.startMarker = container.startCoordinate;
    newMarker.endMarker = container.endCoordinate;
    // console.log(newMarker)
    setMarkers(newMarker);
    setPolyline(container.path);
    setKeyValue(hash({'marker': newMarker, 'path': polyline}));
  }, [
    container.newLocation,
    container.startCoordinate,
    container.endCoordinate,
    container.path,
    markers,
    polyline
  ]);

  const blackOptions = { color: 'blue', weight: '6' }

  return (
    <MapContainer
      center={zoomLocation}
      zoom={13}
      scrollWheelZoom={false}
      className="mainMap"
      key={keyValue}
    >
      <TileLayer
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      {markers.startMarker.length === 0 || polyline.length > 0 ? (
        <></>
      ) : (
        <Marker
          position={markers.startMarker}
        />
      )}
      {markers.endMarker.length === 0  || polyline.length > 0 ? (
        <></>
      ) : (
        <Marker
          position={markers.endMarker}
        />
      )}
      {
        getLineMarkers(polyline).map((ele, key) => <Marker position={ele} key={key}/>)
      }
      <Polyline pathOptions={blackOptions} positions={polyline} />
    </MapContainer>
  );
};
