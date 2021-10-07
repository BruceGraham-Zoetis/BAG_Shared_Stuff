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

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import org.openapitools.client.model.EventInfo;

/**
 * ResponseCurrentlyActivatedEvents200
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2021-10-07T10:16:52.817798-04:00[America/Nassau]")
public class ResponseCurrentlyActivatedEvents200 {
  public static final String SERIALIZED_NAME_CURRENTLY_ACTIVATED_EVENTS = "currently_activated_events";
  @SerializedName(SERIALIZED_NAME_CURRENTLY_ACTIVATED_EVENTS)
  private List<EventInfo> currentlyActivatedEvents = new ArrayList<EventInfo>();


  public ResponseCurrentlyActivatedEvents200 currentlyActivatedEvents(List<EventInfo> currentlyActivatedEvents) {
    
    this.currentlyActivatedEvents = currentlyActivatedEvents;
    return this;
  }

  public ResponseCurrentlyActivatedEvents200 addCurrentlyActivatedEventsItem(EventInfo currentlyActivatedEventsItem) {
    this.currentlyActivatedEvents.add(currentlyActivatedEventsItem);
    return this;
  }

   /**
   * An array of all events that are currently activated
   * @return currentlyActivatedEvents
  **/
  @javax.annotation.Nonnull
  @ApiModelProperty(required = true, value = "An array of all events that are currently activated")

  public List<EventInfo> getCurrentlyActivatedEvents() {
    return currentlyActivatedEvents;
  }


  public void setCurrentlyActivatedEvents(List<EventInfo> currentlyActivatedEvents) {
    this.currentlyActivatedEvents = currentlyActivatedEvents;
  }


  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ResponseCurrentlyActivatedEvents200 responseCurrentlyActivatedEvents200 = (ResponseCurrentlyActivatedEvents200) o;
    return Objects.equals(this.currentlyActivatedEvents, responseCurrentlyActivatedEvents200.currentlyActivatedEvents);
  }

  @Override
  public int hashCode() {
    return Objects.hash(currentlyActivatedEvents);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ResponseCurrentlyActivatedEvents200 {\n");
    sb.append("    currentlyActivatedEvents: ").append(toIndentedString(currentlyActivatedEvents)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}

