package com.zoetis.hub.platform.service;

import java.util.HashMap;
import java.util.Map;

import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.common.serialization.StringSerializer;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.kafka.core.DefaultKafkaProducerFactory;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.kafka.core.ProducerFactory;
import org.springframework.kafka.support.serializer.JsonSerializer;

//import com.zoetis.hub.platform.dto.PrintFileDto;
import com.zoetis.hub.platform.dto.PrintJobStateDto;

@Configuration
public class KafkaConfiguration {
	
	@Value("${spring.kafka.consumer.bootstrap-servers}")
    private String bootstrapServers;
	
	/////////////////////////////////////////////////////////////////////////////////////
	// Consumer PrintFileDto
	/*
	@Bean
    public ConsumerFactory<String, PrintFileDto> consumerFactory4() {
        Map<String, Object> config = new HashMap<>();
        config.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, bootstrapServers);
        config.put(ConsumerConfig.GROUP_ID_CONFIG, "groupPrinterAccess");
		config.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class);
		config.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, JsonDeserializer.class);
        
        return new DefaultKafkaConsumerFactory<>(config, new StringDeserializer(),
                new JsonDeserializer<>(PrintFileDto.class));
    }
    
    @Bean
    public ConcurrentKafkaListenerContainerFactory<String, PrintFileDto> kafkaListenerContainerFactory() {
        ConcurrentKafkaListenerContainerFactory<String, PrintFileDto>
                factory = new ConcurrentKafkaListenerContainerFactory<>();
        factory.setConsumerFactory(consumerFactory4());
        return factory;
    }
    */

	/////////////////////////////////////////////////////////////////////////////////////
	// Producer PrintJobStateDto
	public ProducerFactory<String, PrintJobStateDto> producerFactory2() {
		Map<String, Object> config = new HashMap<>();
		config.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, bootstrapServers);
		config.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class);
		config.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, JsonSerializer.class);

		return new DefaultKafkaProducerFactory<>(config);
	}

	@Bean
	public KafkaTemplate<String, PrintJobStateDto> kafkaTemplate2() {
		return new KafkaTemplate<>(producerFactory2());
	}
	
}