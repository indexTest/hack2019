package ca.ix.hackathon.dao;

public class MatcherResponse {
	private String uuid;
	private String pid;
	private double lat;
	private double lon;
	
	
	
	public MatcherResponse(String uuid, String pid, double lat, double lon) {
		super();
		this.uuid = uuid;
		this.pid = pid;
		this.lat = lat;
		this.lon = lon;
	}
	public String getPid() {
		return pid;
	}
	public void setPid(String pid) {
		this.pid = pid;
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
	public String getUuid() {
		return uuid;
	}
	public void setUuid(String uuid) {
		this.uuid = uuid;
	}
	
	

}
