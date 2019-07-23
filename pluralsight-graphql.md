**GraphQL** is a query language that is an alternative to REST

[https://www.graphqlhub.com](https://www.graphqlhub.com) is a great website with some demos to try out graphql queries



```graphql
# It's generally a good idea to name your query so that you may easily find it later
query demo_query
#after naming our query, we'll start our selection set by using brackets
{
  # first named items are root nodes for us to query data about
  # notice that we can have multiple root nodes
  
  # graphQLHub is a scalar field so we don't need a sub selection
  graphQLHub
  # querying github by itself will result in an error because we need a sub selection
  # github
  github {
    user(username: "bjellesma"){
      avatar_url
      repos{
        name
        commits {
          message
          date
        }
      }
    }
  }
  twitter {
    user (identifier: name, identity: "clayallsopp") {
      created_at
      description
      id
      screen_name
      name
      profile_image_url
      url
      tweets_count
      followers_count
      tweets(limit: 1) {
        text
      }
    }
    tweet(id: "687433440774459392") {
      text,
      retweets(limit: 2) {
        id,
        retweeted_status {
          id
        }
        user {
          screen_name
        }
      }
    }
    search(q: "Javascript", count: 1, result_type: mixed) {
      user {
        screen_name
      }
      id
      text
    }
  }
}
```

# Query Variables

```sql
query TestQuery($username: String!){
  github {
    user(username: $username) {
      login
      id
      avatar_url
    }
  }
}
```

Define your variables in the variable section on graphqlhub

```graphql
{
  "username": "bjellesma"
}
```

As you can see, you can define variables in a friendly json syntax

# Fragments

Fragments are reusable parts of queries. This helps performance on the front end because you can now split complicated api queries into smaller reusable chunks. 

# Directives

Directives are specified as `@includeif` and `@skip`, you can imagine that these add logic to applications by only executing the query if a certain boolean is true.

# Mutations

Mutations are used to explicity get data AFTER an update by using GrphQL
