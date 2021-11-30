package com.skcnc.backend.dto;

import javax.persistence.Id;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class TokenCheckRequest {
    @Id
    private String accessToken;
}
