/*
 * Analyzer and HUB API
 * The definition of the software interface between analyzers and the HUB.  The interface will be implemented as a RESTful interface with all server endpoints hosted on the Analyzer.  The following requirements will be met by all interfaces:  1. All data passed back from server shall be in JSON format. 2. All query parameters and JSON data properties shall be named using snake case and be all lower case. 4. All data types that describe a measurement value shall end with an underscore followed by the unit of that physical value.  i.e. motor_current_ma.
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.ResponseStatusOperational200;
import org.junit.Test;
import org.junit.Ignore;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for StatusChannelApi
 */
@Ignore
public class StatusChannelApiTest {

    private final StatusChannelApi api = new StatusChannelApi();

    
    /**
     * 
     *
     * The HUB can use send this message to get the status of an analyzer
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void statusGetTest() throws ApiException {
        ResponseStatusOperational200 response = api.statusGet();

        // TODO: test validations
    }
    
}
