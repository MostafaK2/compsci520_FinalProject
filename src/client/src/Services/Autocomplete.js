import { OpenStreetMapProvider } from 'leaflet-geosearch';

const provider = new OpenStreetMapProvider();

export const getMatchedResults = async (value) => {
    const results = await provider.search({ query: value });

    return results;
} 
