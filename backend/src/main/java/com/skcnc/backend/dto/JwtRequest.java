package com.skcnc.backend.dto;

import javax.persistence.Id;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class JwtRequest {
    @Id
    private String id;
    private String password;
}