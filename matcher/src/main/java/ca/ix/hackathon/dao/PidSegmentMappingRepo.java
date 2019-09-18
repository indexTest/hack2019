package ca.ix.hackathon.dao;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import ca.ix.hackathon.model.PidSegmentMapping;

public interface PidSegmentMappingRepo extends JpaRepository<PidSegmentMapping,Integer> {
	
	List<PidSegmentMapping> findByPid(String pid);

}
