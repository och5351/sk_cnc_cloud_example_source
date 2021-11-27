package com.skcnc.backend.repository;

import com.skcnc.backend.domain.Member;

import org.springframework.data.mongodb.repository.MongoRepository;

public interface MemberRepository extends MongoRepository<Member, String> {
}
