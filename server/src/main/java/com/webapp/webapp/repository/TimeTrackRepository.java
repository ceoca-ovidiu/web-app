package com.webapp.webapp.repository;

import com.webapp.webapp.model.TimeTrack;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface TimeTrackRepository extends MongoRepository<TimeTrack, String> {
}
