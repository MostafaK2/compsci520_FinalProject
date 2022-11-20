import { MapContainer, useMapEvent } from "react-leaflet";

function ClickComponent() {
    const map = useMapEvent('click', () => {
      map.setCenter([50.5, 30.5])
    })
    return null
  }

export const Map = () => {
  return (
    <MapContainer center={[50.5, 30.5]} zoom={13}>
      <ClickComponent />
    </MapContainer>
  );
};
