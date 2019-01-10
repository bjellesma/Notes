LINQ stands for **Language Integrated Query**

# Delegates

Delegates are special types of objects that can use a list of methods.

```csharp
public class Class1
    {
        delegate void MyDelegate(string myString);
        public void showThoseMessages()
        {
            MyDelegate md = new MyDelegate(ShowMessage);
            md += ShowAnotherMessage;
            md("Test");
        }
        void ShowMessage(string message)
        {
            MessageBox.Show(message);
        }
        void ShowAnotherMessage(string message)
        {
            MessageBox.Show(message + "again");
        }
    }
```

# Lambdas and Func

A lambda expression can be described as a *is defined as* operator. A `func` is a special type of function that will take up to 16 generic types, with the last parameter being the return value.
For example,

```csharp
Func<int, int> square = x => x*x;
```

reads that the function square takes an int, returns an int, and x, the parameter, reads "is defined as" x*x. 

**NOTE** the function must return the return type specified, in this case, integer

```csharp
Console.WriteLine(square(3));
//writes 9
```

```csharp
Func<int, int, int> add = (x,y) => x + y;
```

Here, x and y are parameters to be added and return an integer value

```csharp
Console.WriteLine(add(3,3));
//Writes 6
```

# LINQ Expressions

A linq expression will use sql logic on collections to get the result that you desire

```chsare
string[] cities = new[]{"London", "Las Vegas", "Glasgow"}
Console.WriteLine(cities.Where(city => city.StartsWith("L"))
//London, Las Vegas
```

Because linq expressions use SQL logic, the entity framework allows us to connect to a remote datasource.

# Var keyword

var keyword still uses the strongly typed nature of C based languages but lets the compiler use type inferencing to figure the type to assign.
var is not like Javascript var to turn to a weakly typed variable.

