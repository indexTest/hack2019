package ca.ix.hackathon.model;

import javax.persistence.Entity;
import javax.persistence.Id;

@Entity
public class PidSegmentMapping {
	
	@Id
	private int id;
	private String pid;
	private String segmentId;
	private int count;
	
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getSegmentId() {
		return segmentId;
	}
	public void setSegmentId(String segmentId) {
		this.segmentId = segmentId;
	}
	public int getCount() {
		return count;
	}
	public void setCount(int count) {
		this.count = count;
	}
	public String getPid() {
		return pid;
	}
	public void setPid(String pid) {
		this.pid = pid;
	}
	@Override
	public String toString() {
		return "PidSegmentMapping [id=" + id + ", pid=" + pid + ", segmentId=" + segmentId + ", count=" + count + "]";
	}
	

	
	
	
	
}
