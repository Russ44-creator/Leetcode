using System;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

namespace Demo
{
    class Program
    {
        static void Main(string[] args)
        {
            handle_json();
        }

        // See ../1-json-primer.md for an explanation
        static void handle_json()
        {
            string json_text = "{\"foo\": {\"bar\": [{\"nato\": \"oscar\"}, {\"nato\": \"papa\"}, {\"nato\": \"quebec\"}]}}";
            dynamic data = JsonConvert.DeserializeObject(json_text);

            string nato_letter = data.foo.bar[1].nato;  // "papa"
            Console.WriteLine(nato_letter);

            // data["foo"]["quux"] = {"stuff": "nonsense", "nums": [2.718, 3.142]}
            data.foo.quux = JObject.FromObject(
                new {
                    stuff = "nonsense",
                    nums = new[] {2.718, 3.142}
                }
            );

            string result = JsonConvert.SerializeObject(data, Formatting.Indented);
            Console.WriteLine(result);
        }
    }
}
