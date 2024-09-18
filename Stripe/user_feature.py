'''
Consider a system of User and Feature objects, where a Feature describes the availability of
an ongoing project or change in functionality. Features may be generally available, limited to
certain regions, and/or intended for an A/B test. We need to write a deterministic system for
identifying which Features are active for a given User. We also want to write tests to ensure
that our system is working as intended each time we run it, given the example User and Feature
data below.
Users:
[
{ "id": 0, "name": "eva", "location": "US" },
{ "id": 1, "name": "tess", "location": "US" },
{ "id": 2, "name": "rahool", "location": "CA" },
{ "id": 3, "name": "amanda", "location": "CA" }
]
Features:
[
{
    "id": "annual_sale",
    "locations": ["US"],
    "abTest": true,
},
{
    "id": "enhanced_comments",
    "abTest": true,
},
{
    "id": "canada_promotion",
    "locations": ["CA"],
}
]

## Part 1
Write a function, `get_user_features(user, features)` which takes a single User object and a list
of Feature objects and returns a set of the Feature IDs that apply to the given User.
A User has three properties: an integer `id`, a string `name`, and a 2-letter country code
string `location`.
A Feature has three properties: a unique string `id`, an optional array of 2-letter country code
strings, `locations`, which limits the feature to users with a matching location, and an optional
boolean, `abTest`, which when set to true will only apply the feature to users with an even user ID.
If `abTest` or `locations` are absent for a Feature, they have no effect.
Given the features and users, the following results are expected:
| User| Features|
| ------ | ----------------------------------- |
| eva| annual_sale, enhanced_comments|
| tess| N/A|
| rahool | enhanced_comments, canada_promotion |
| amanda | canada_promotion|
'''

user = { "id": 0, "name": "eva", "location": "US" }
features = [
    { "id": "annual_sale", "locations": ["US"], "abTest": True },
    { "id": "enhanced_comments", "abTest": True },
    { "id": "canada_promotion", "locations": ["CA"] }
]
def get_user_features(user, features):
    abtest_ans, location_ans = [], []
    for feature in features:
        if "abTest" in feature and feature["abTest"]:
            if user["id"] % 2 == 0:
                abtest_ans.append(feature["id"])
        else:
            abtest_ans.append(feature["id"])
        if "locations" in feature:
            if user["location"] in feature["locations"]:
                location_ans.append(feature["id"])
        else:
            location_ans.append(feature["id"])
    return list(set(abtest_ans) & set(location_ans))

print(get_user_features(user, features))

'''
## Part 2
Users may want to opt-in to or opt-out of a feature. Augment `get_user_features` to take into
account two new properties on `User` objects: `optIn` and `optOut`, both of which are arrays of
feature IDs to either opt into or opt out of. A user can be opted-in to an A/B test Feature,
regardless of their ID. A user cannot be given a feature that is not available in their region,
even if they try to opt-in to it.
Users 0 (eva), 1 (tess) and 3 (amanda) would like to opt in to the `annual_sale` feature.
User 2, (rahool), would like to opt out of the `enhanced_comments` and `canada_promotion` features.
Our new user data is...
Users:
{ "id": 0, "name": "eva", "location": "US", "optIn": ["annual_sale"] }
{ "id": 1, "name": "tess", "location": "US", "optIn": ["annual_sale"] }
{ "id": 2, "name": "rahool", "location": "CA", "optOut": ["enhanced_comments", "canada_promotion"] }
{ "id": 3, "name": "amanda", "location": "CA", "optIn": ["annual_sale"] }
Given these changes and updates, the following results are now expected:
| User| Features
| ------ | ------------------------------ |
| eva| annual_sale, enhanced_comments |
| tess| annual_sale|
| rahool | N/A|
| amanda | canada_promotion|
'''

"""
## Part 3
Sometimes, Features have conflicts with each other. To prevent a broken experience for users, we need
to make sure Features don't collide with other Features they shouldn't be active alongside. Augment
`get_user_features` to take into account two new properties on `Feature` objects: `incompatible` and
`priority`. A Feature cannot be enabled for a User if another Feature in its `incompatible` list is
also active for the User. In this case, the Feature with the higher `priority` will be activated. A
feature with no specified `priority` is priority 0. Higher priority values take precedence.
If a user has opted-in to a feature, that feature takes priority over all other features if there
is an incompatibility.
We are adding a new feature called `lunar_sale` which is incompatible with `annual_sale` and has a
priority of 10 and no location restrictions.
We are also adding a new feature called `app_redesign` which is an A/B tested feature and incompatible
with `lunar_sale` and `enhanced_comments`. It has a priority of 15.
Our new feature data is...
[
    {
        "id": "annual_sale",
        "locations": ["US"],
        "abTest": true,
    },
    {
        "id": "enhanced_comments",
        "abTest": true,
    },
    {
        "id": "canada_promotion",
        "locations": ["CA"],
    },
    {
        "id": "lunar_sale",
        "incompatible": ["annual_sale"],
        "priority": 10,
    },
    {
        "id": "app_redesign",
        "incompatible": ["lunar_sale", "enhanced_comments"],
        "priority": 15,
        "abTest": true
    },
]
Given these additional features, the following results are now expected:
| User   | Features                       |
| ------ | ---------------------------- |
| eva    | app_redesign, annual_sale    |
| tess   | annual_sale                  |
| rahool | app_redesign                 |
| amanda | lunar_sale, canada_promotion |
"""
