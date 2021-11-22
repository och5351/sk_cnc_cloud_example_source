package com.skcnc.backend.controller;

import com.skcnc.backend.service.CrawlerService;

import java.io.IOException;

import com.skcnc.backend.model.request.CrawlerRequest;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import lombok.RequiredArgsConstructor;

@RestController
@RequestMapping(value = "/api/crawler")
@RequiredArgsConstructor
public class CrawlerController {

    private final CrawlerService crawlerService;

    @PostMapping("/search")
    @ResponseBody
    public String crawlering(CrawlerRequest request) throws IOException, InterruptedException {
        Boolean test = crawlerService.search_service(request);
        if (test) {
            return "크롤링을 완료했습니다.";
        } else {
            return "크롤링을 실패했습니다.";
        }

    }

}
