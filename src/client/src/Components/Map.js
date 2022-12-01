import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import L from "leaflet";
import "leaflet/dist/leaflet.css";
import icon from "leaflet/dist/images/marker-icon.png";
import iconShadow from "leaflet/dist/images/marker-shadow.png";
import { Container } from "../Store/Provider";
import { useState, useEffect } from "react";

let DefaultIcon = L.icon({
  iconUrl: icon,
  shadowUrl: iconShadow,
});

L.Marker.prototype.options.icon = DefaultIcon;

export const Map = () => {
  const [zoomLocation, setZoomLocation] = useState([42.3754, -72.5193]);
  const [markers, setMarkers] = useState({ startMarker: [], endMarker: [] });
  const container = Container.useContainer();

  useEffect(() => {
    setZoomLocation(container.newLocation);
    console.log(markers);
    let newMarker = markers;
    newMarker.startMarker = container.startCoordinate;
    newMarker.endMarker = container.endCoordinate;
    setMarkers(newMarker);
  }, [
    container.newLocation,
    container.startCoordinate,
    container.endCoordinate,
  ]);

  return (
    <MapContainer
      center={zoomLocation}
      zoom={10}
      scrollWheelZoom={false}
      className="mainMap"
      key={`${zoomLocation[0]}-${zoomLocation[1]}`}
    >
      <TileLayer
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      {markers.startMarker.length == 0 ? (
        <></>
      ) : (
        <Marker
          position={markers.startMarker}
        />
      )}
      {markers.endMarker.length == 0 ? (
        <></>
      ) : (
        <Marker
          position={markers.endMarker}
        />
      )}
    </MapContainer>
  );
};
