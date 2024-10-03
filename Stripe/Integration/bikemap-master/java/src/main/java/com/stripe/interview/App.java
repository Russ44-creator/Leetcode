package com.stripe.interview;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

import com.jsoniter.JsonIterator;
import com.jsoniter.any.Any;
import com.jsoniter.output.JsonStream;
import com.jsoniter.spi.Config;

public class App 
{
    public static void main( String[] args )
    {
        handle_json();
    }

    // See 1-json-primer.md for an explanation
    public static void handle_json()
    {
        String json_text = "{\"foo\": {\"bar\": [{\"nato\": \"oscar\"}, {\"nato\": \"papa\"}, {\"nato\": \"quebec\"}]}}";
        Any data = JsonIterator.deserialize(json_text);

        // Use toString(), toDouble(), toInt(), etc with types
        String natoLetter = data.toString("foo", "bar", 1, "nato");
        System.out.printf("toString: %s\n", natoLetter); // "papa"

        // Or use get() and Any
        Any natoLetter2 = data.get("foo", "bar", 1, "nato");
        System.out.printf("Any: %s\n", natoLetter2); // "papa"

        // Can also use Map.of for homogenous key-value pairs in Java 9+
        Map<String, Object> quux = new HashMap<>();
        quux.put("stuff", "nonsense");
        quux.put("nums", Arrays.asList(2.718, 3.142));

        // data["foo"]["quux"] = {"stuff": "nonsense", "nums": [2.718, 3.142]}
        data.get("foo").asMap().put("quux", Any.wrap(quux));

        // Use Config to get pretty-printed indentation
        Config cfg = new Config.Builder().indentionStep(2).build();

        // serialize object to string as json
        String result = JsonStream.serialize(cfg, data);
        System.out.println(result);
    }
}
