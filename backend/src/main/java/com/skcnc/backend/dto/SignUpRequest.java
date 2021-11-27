package com.skcnc.backend.dto;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class SignUpRequest {

    private String id;
    private String password;
    private String name;
}
