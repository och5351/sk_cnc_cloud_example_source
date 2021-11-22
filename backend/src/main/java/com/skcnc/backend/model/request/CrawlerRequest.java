package com.skcnc.backend.model.request;

import lombok.Data;

@Data
public class CrawlerRequest {
    private String search_test;
    private int page_num;
}
