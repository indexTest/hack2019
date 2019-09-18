package ca.ix.hackathon.controller;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.UUID;

import org.json.simple.parser.ParseException;
import org.springframework.beans.factory.annotation.Autowired;
import ca.ix.hackathon.model.*;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import ca.ix.hackathon.dao.LocationResponse;
import ca.ix.hackathon.dao.MatcherResponse;
import ca.ix.hackathon.dao.PidSegmentMappingRepo;
import ca.ix.hackathon.utils.CommonUtils;

@Controller
public class PidSegmentMappingController {
	
	@Autowired
	PidSegmentMappingRepo pidSegmentMapping;
	
@RequestMapping("/")
@ResponseBody
public String home() {
	
	CommonUtils c = new CommonUtils();
	System.out.println("Distance is : "+ c.distance(32.9697, -96.80322, 29.46786, -98.53506, "M"));
	
	System.out.println(pidSegmentMapping.findByPid("mark"));
	return pidSegmentMapping.findByPid("mark").toString();
		//return "home.jsp";
	}


@RequestMapping("/getMatcher")
@ResponseBody
public MatcherResponse getMatcher(@RequestParam String pid, @RequestParam double lat, @RequestParam double lon, @RequestParam String mode,
		@RequestParam int countToReturn,@RequestParam int threshold) throws ParseException 
{
	List<List<PidSegmentMapping>> peopleWhoAreNearMappings= new ArrayList<List<PidSegmentMapping>>();
	CommonUtils c = new CommonUtils();
	List<PidSegmentMapping> mapping = pidSegmentMapping.findByPid(pid);
	List<LocationResponse> peopleNearThisPerson = c.getPeopleCloserToPid(pid, lat, lon);
	
	Map<String,List<String>> pidSegmentsMap= new HashMap<>();
	Map<String, Integer> finalMatchingMap= new HashMap<>();
	
	if(mapping.size()==0) {
		System.out.println("Mapping not found");
		return (new MatcherResponse(null,null,-1,-1));
	}
	List<String> sourcePersonSegmentList= new ArrayList<>();
	for(PidSegmentMapping eachMapping: mapping) {
		sourcePersonSegmentList.add(eachMapping.getSegmentId());
	}


	
	for(LocationResponse eachPerson : peopleNearThisPerson) {
		List<String> segmentList= new ArrayList<>();
		List<PidSegmentMapping> peoples = pidSegmentMapping.findByPid(eachPerson.getPid());
		for(PidSegmentMapping people: peoples) {
			segmentList.add(people.getSegmentId());
		}
		peopleWhoAreNearMappings.add(pidSegmentMapping.findByPid(eachPerson.getPid()));
		pidSegmentsMap.put(eachPerson.getPid(), segmentList);
	}
	
	//loop through each hash map entry and do the comparison of list
	for(Map.Entry<String, List<String>> entry: pidSegmentsMap.entrySet()) {
		ArrayList<String> commonSegments= new ArrayList<>(sourcePersonSegmentList);
		commonSegments.retainAll(entry.getValue());
		//add to a new map which has common sengments count and pid
		//
		finalMatchingMap.put(entry.getKey(), commonSegments.size());
		
	}
	
	System.out.println("pidSegmentsMap: "+  pidSegmentsMap.toString());
	System.out.println("sourcePersonSegmentList: "+sourcePersonSegmentList.toString());
	System.out.println("finalMatchingMap: "+finalMatchingMap.toString());
	
	String matchKey = finalMatchingMap.entrySet().stream().max((entry1, entry2) -> entry1.getValue() > entry2.getValue() ? 1 : -1).get().getKey();

	String uuid = UUID.randomUUID().toString();
	LocationResponse matchedPerson = getLocation(matchKey);
	
	
		return new MatcherResponse(uuid, matchedPerson.getPid(),matchedPerson.getLat(), matchedPerson.getLon());
	}


@RequestMapping("/getLocationByPid/{pid}")	
@ResponseBody
public LocationResponse getLocation(@PathVariable("pid") String pid) {
	
	CommonUtils c = new CommonUtils();

	try {
		System.out.println(c.getLocationByPid(pid));
		return c.getLocationByPid(pid);
	} catch (ParseException e) {
		e.printStackTrace();
		return null;
	}
		
	}

}
