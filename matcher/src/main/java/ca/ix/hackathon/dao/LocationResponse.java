package ca.ix.hackathon.dao;

public class LocationResponse {
	String pid;
	double lat;
	double lon;
	
	public LocationResponse(String pid, double lat, double lon) {
		super();
		this.pid= pid;
		this.lat = lat;
		this.lon = lon;
	}
	public double getLat() {
		return lat;
	}
	public void setLat(double lat) {
		this.lat = lat;
	}
	public double getLon() {
		return lon;
	}
	public void setLon(double lon) {
		this.lon = lon;
	}
	
	public String getPid() {
		return pid;
	}
	public void setPid(String pid) {
		this.pid = pid;
	}
	@Override
	public String toString() {
		return "LocationResponse [pid=" + pid + ", lat=" + lat + ", lon=" + lon + "]";
	}
	
	
	
	

}
