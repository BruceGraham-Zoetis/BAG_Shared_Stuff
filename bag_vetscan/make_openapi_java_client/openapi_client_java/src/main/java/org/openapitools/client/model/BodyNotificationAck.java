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

/**
 * BodyNotificationAck
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2021-10-07T10:16:52.817798-04:00[America/Nassau]")
public class BodyNotificationAck {
  public static final String SERIALIZED_NAME_CORRELATION_ID = "correlation_id";
  @SerializedName(SERIALIZED_NAME_CORRELATION_ID)
  private String correlationId;


  public BodyNotificationAck correlationId(String correlationId) {
    
    this.correlationId = correlationId;
    return this;
  }

   /**
   * A unique ID that can be used to correlate messages being sent and received
   * @return correlationId
  **/
  @javax.annotation.Nonnull
  @ApiModelProperty(example = "ABC123", required = true, value = "A unique ID that can be used to correlate messages being sent and received")

  public String getCorrelationId() {
    return correlationId;
  }


  public void setCorrelationId(String correlationId) {
    this.correlationId = correlationId;
  }


  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    BodyNotificationAck bodyNotificationAck = (BodyNotificationAck) o;
    return Objects.equals(this.correlationId, bodyNotificationAck.correlationId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(correlationId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class BodyNotificationAck {\n");
    sb.append("    correlationId: ").append(toIndentedString(correlationId)).append("\n");
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

