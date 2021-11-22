package com.skcnc.backend.service;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

import com.skcnc.backend.model.request.CrawlerRequest;
import org.springframework.stereotype.Service;
import lombok.RequiredArgsConstructor;

@Service
@RequiredArgsConstructor
public class CrawlerService {

    public Boolean search_service(CrawlerRequest crawlerRequest) {

        try {
            String script_kind = null;
            String file_path = null;
            if (System.getProperty("os.name").indexOf("Windows") > -1) {
                script_kind = "cmd";
                file_path = "..\\www_crawler\\dist\\Fetch_Controller.exe";
            } else {
                script_kind = "sh";
                file_path = "../www_crawler/dist/Fetch_Controller.exe";
            }
            ProcessBuilder p = new ProcessBuilder(script_kind);
            p.redirectErrorStream(true);
            Process process = p.start();
            BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(process.getOutputStream(), "euc-kr"));
            writer.write(file_path + "\n");
            writer.flush();
            writer.write(crawlerRequest.getSearch_test() + " " + crawlerRequest.getPage_num() + "\n");
            writer.flush();
            String str = null;
            BufferedReader stdOut = new BufferedReader(new InputStreamReader(process.getInputStream(), "euc-kr"));
            while ((str = stdOut.readLine()) != null) {
                if (str.trim().equals("stop_crawler_program")) {
                    break;
                }
                System.out.println(str);
            }
            process.destroy();
        } catch (IOException e) {
            e.printStackTrace();
            return false;
        }

        return true;
    }
}
