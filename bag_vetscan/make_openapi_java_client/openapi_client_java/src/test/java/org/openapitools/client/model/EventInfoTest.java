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


package org.openapitools.client.model;

import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;
import org.junit.Assert;
import org.junit.Ignore;
import org.junit.Test;


/**
 * Model tests for EventInfo
 */
public class EventInfoTest {
    private final EventInfo model = new EventInfo();

    /**
     * Model tests for EventInfo
     */
    @Test
    public void testEventInfo() {
        // TODO: test EventInfo
    }

    /**
     * Test the property 'activationTime'
     */
    @Test
    public void activationTimeTest() {
        // TODO: test activationTime
    }

    /**
     * Test the property 'severity'
     */
    @Test
    public void severityTest() {
        // TODO: test severity
    }

    /**
     * Test the property 'eventName'
     */
    @Test
    public void eventNameTest() {
        // TODO: test eventName
    }

    /**
     * Test the property 'eventAdditionalInformation'
     */
    @Test
    public void eventAdditionalInformationTest() {
        // TODO: test eventAdditionalInformation
    }

}
