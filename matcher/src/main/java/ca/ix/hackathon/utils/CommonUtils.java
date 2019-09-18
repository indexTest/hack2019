package ca.ix.hackathon.utils;


import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.text.ParseException;
import java.util.ArrayList;
import java.util.List;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

import ca.ix.hackathon.dao.LocationResponse;

public final class CommonUtils {
	
	public double distance(double lat1, double lon1, double lat2, double lon2, String unit) {
		  double theta = lon1 - lon2;
		  double dist = Math.sin(deg2rad(lat1)) * Math.sin(deg2rad(lat2)) + Math.cos(deg2rad(lat1)) * Math.cos(deg2rad(lat2)) * Math.cos(deg2rad(theta));
		  dist = Math.acos(dist);
		  dist = rad2deg(dist);
		  dist = dist * 60 * 1.1515;
		  if (unit == "M") {
		    dist = dist * 1.609344 * 1000;
		  } else if (unit == "N") {
		  dist = dist * 0.8684;
		    }
		  return (dist);
		}
		
	
	/*:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::*/
	/*::  This function converts decimal degrees to radians             :*/
	/*:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::*/
	private double deg2rad(double deg) {
		  return (deg * Math.PI / 180.0);
		}
	/*:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::*/
	/*::  This function converts radians to decimal degrees             :*/
	/*:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::*/
	private double rad2deg(double rad) {
		  return (rad * 180.0 / Math.PI);
		}


	public LocationResponse getLocationByPid(String pid) throws org.json.simple.parser.ParseException {
		JSONParser jsonParser = new JSONParser();
		List<LocationResponse> locations = new ArrayList<LocationResponse>();
		
		try (FileReader reader = new FileReader("src/main/resources/people.json"))
				//new FileReader("/home/james_chen/people.json"))
        {
            //Read JSON file
            Object obj = jsonParser.parse(reader);
 
            JSONArray pidList = (JSONArray) obj;
            System.out.println(pidList);
             
            pidList.forEach( emp -> parsePidObject((JSONObject) emp, pid, locations));
            System.out.println(locations.toString());
            System.out.println(locations.size());
            return locations.get(0);
 
        } catch (FileNotFoundException e) {
            e.printStackTrace();
            return null;
            
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }
		
	
	}


	private void parsePidObject(JSONObject PidObj, String pid_from_restCall, List<LocationResponse> locations) {
		Double lat = (Double) PidObj.get("lat"); 
		Double lon = (Double) PidObj.get("lon");
		String pid= (String) PidObj.get("pid");
		//System.out.println(lat);
		//System.out.println(lon);
		//System.out.println(pid);
		
		if(pid.equalsIgnoreCase(pid_from_restCall)) {
			System.out.println("in if");
			locations.add(new LocationResponse(pid,lat,lon));
		}
		System.out.println("in else return");
	}
	
	
	public List<LocationResponse> getPeopleCloserToPid(String pid, double lat, double lon) 
			throws org.json.simple.parser.ParseException { 
		JSONParser jsonParser = new JSONParser();
		List<LocationResponse> locations = new ArrayList<LocationResponse>();

		try (FileReader reader = new FileReader("src/main/resources/people.json"))
				//new FileReader("/home/james_chen/people.json"))
        {
            //Read JSON file
            Object obj = jsonParser.parse(reader);
 
            JSONArray pidList = (JSONArray) obj;
            System.out.println(pidList);
             
            pidList.forEach( emp -> parsePidObjectForDistance((JSONObject) emp, pid,lat, lon , locations));
            System.out.println(locations.toString());
            System.out.println(locations.size());
            return locations;
 
        } catch (FileNotFoundException e) {
            e.printStackTrace();
            return null;
            
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }
		
		
	}
	
	private void parsePidObjectForDistance(JSONObject PidObj, String pid_from_restCall,double lat_from_restCall,
			double lon_from_restCall, List<LocationResponse> locations) {
		
		Double lat = (Double) PidObj.get("lat"); 
		Double lon = (Double) PidObj.get("lon");
		String pid= (String) PidObj.get("pid");
		
		double distance= distance(lat, lon, lat_from_restCall, lon_from_restCall, "M");
		
		System.out.println("distance= "+distance);
	
		System.out.println(pid_from_restCall+ ": "+pid);
		if(pid.equalsIgnoreCase(pid_from_restCall)) return;
		
		if(distance<=222380) {
			System.out.println("in if");
			locations.add(new LocationResponse(pid,lat,lon));
		}
		//System.out.println("in else return");
	}
	
}
