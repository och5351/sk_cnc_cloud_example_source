package com.skcnc.backend.controller;

import com.skcnc.backend.dto.IdCheckRequest;
import com.skcnc.backend.dto.JwtRequest;
import com.skcnc.backend.dto.JwtResponse;
import com.skcnc.backend.dto.SignUpRequest;
import com.skcnc.backend.service.MemberService;
import lombok.AllArgsConstructor;

import org.json.simple.JSONObject;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping(value = "/api/member")
@AllArgsConstructor
public class MemberController {
    public final MemberService memberService;

    @PostMapping(value = "/signin", produces = MediaType.APPLICATION_JSON_VALUE)
    public JwtResponse signIn(@RequestBody JwtRequest request) {
        try {
            return memberService.signIn(request);
        } catch (Exception e) {
            return new JwtResponse(e.getMessage());
        }
    }

    @PostMapping(value = "/idCheck", produces = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<JSONObject> idCheck(@RequestBody IdCheckRequest request) {
        return ResponseEntity.ok(memberService.idCheck(request));
    }

    @PostMapping(value = "/signup", produces = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<Boolean> signup(@RequestBody SignUpRequest request) {
        return memberService.signup(request);
    }

}
