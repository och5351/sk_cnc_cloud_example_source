package com.skcnc.backend.service;

import lombok.AllArgsConstructor;

import com.skcnc.backend.domain.Member;
import com.skcnc.backend.dto.IdCheckRequest;
import com.skcnc.backend.dto.JwtRequest;
import com.skcnc.backend.dto.JwtResponse;
import com.skcnc.backend.dto.SignUpRequest;
import com.skcnc.backend.repository.MemberRepository;
import com.skcnc.backend.security.JwtTokenProvider;
import com.skcnc.backend.security.UserDetailsImpl;
import org.json.simple.JSONObject;
import org.springframework.http.ResponseEntity;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
@Transactional
@AllArgsConstructor
public class MemberService {
    private final MemberRepository memberRepository;
    private final PasswordEncoder passwordEncoder;
    private final AuthenticationManager authenticationManager;
    private final JwtTokenProvider jwtTokenProvider;

    public JwtResponse signIn(JwtRequest request) throws Exception {
        Authentication authentication = authenticationManager
                .authenticate(new UsernamePasswordAuthenticationToken(request.getId(),
                        request.getPassword()));

        return createJwtToken(authentication);

    }

    private JwtResponse createJwtToken(Authentication authentication) {
        UserDetailsImpl principal = (UserDetailsImpl) authentication.getPrincipal();

        String token = jwtTokenProvider.generateToken(principal);
        return new JwtResponse(token);
    }

    public JSONObject idCheck(IdCheckRequest request) {
        boolean existMember = memberRepository.existsById(request.getId());
        JSONObject json = new JSONObject();
        json.put("success", existMember); // put을 통해 데이터를 보내준다.
        if (existMember)
            json.put("message", "아이디가 중복 됩니다.");
        else
            json.put("message", "사용 가능한 아이디 입니다.");

        return json;
    }

    public ResponseEntity<Boolean> signup(SignUpRequest request) {

        boolean existMember = memberRepository.existsById(request.getId());

        // 이미 회원이 존재하는 경우
        if (existMember)
            return null;

        Member member = new Member(request);
        member.encryptPassword(passwordEncoder);

        memberRepository.save(member);
        return ResponseEntity.ok(!existMember);

    }
}
