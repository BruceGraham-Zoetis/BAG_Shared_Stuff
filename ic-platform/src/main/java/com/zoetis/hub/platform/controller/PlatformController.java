package com.zoetis.hub.platform.controller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import com.zoetis.hub.platform.service.Producer;

@Controller
@RequestMapping("")
public class PlatformController
{
	@Autowired
	Producer producer;

	static Logger logger = LoggerFactory.getLogger (com.zoetis.hub.platform.controller.PlatformController.class);
	
    @GetMapping("/")
    public String home ()
    {
        return "home";
    }
}


