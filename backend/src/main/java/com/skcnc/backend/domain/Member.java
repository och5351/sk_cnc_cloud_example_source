package com.skcnc.backend.domain;

import javax.persistence.*;

import com.skcnc.backend.dto.SignUpRequest;
import com.skcnc.backend.model.Role;

import org.springframework.data.mongodb.core.mapping.Document;
import org.springframework.security.crypto.password.PasswordEncoder;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@Entity
@NoArgsConstructor
@Document(collection = "member")
public class Member {

    @Id
    private String id;
    private String password;
    private String name;

    @Enumerated(EnumType.STRING)
    private Role role;

    public Member(SignUpRequest request) {
        this.password = request.getPassword();
        this.name = request.getName();
        this.id = request.getId();
        this.role = Role.USER;
    }

    public void encryptPassword(PasswordEncoder passwordEncoder) {
        this.password = passwordEncoder.encode(password);
    }
}
