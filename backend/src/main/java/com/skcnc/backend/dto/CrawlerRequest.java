package com.skcnc.backend.dto;

import lombok.Data;

@Data
public class CrawlerRequest {
    private String search_test;
    private int page_num;
}
