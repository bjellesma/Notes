## Methods

Overloading a method is valid when you have two methods of the same name but have different parameter types on each. Overloaded methods are useful if you want different behavior in the methods. The following example creates an overload of the WriteResult method
```csharp
static void WriteResult(string description, int result){
  Console.WriteLine(description + " in whole number form: " + result);
}
```
overloads
```csharp
static void WriteResult(string description, float result){
  Console.WriteLine(description + " in decimal number form: " + result);
}
```

Using this knowledge, you can create an overloaded method to take a variable number of arguments by using the `params` keyword

```csharp
static void WriteResult(string description, params float[] results){
  foreach(float result in results){
    Console.WriteLine(description + ": " + result);
  }
}
```

You can use the concept of **formatting strings** to rewrite the above override method as follows

```csharp
static void WriteResult(string description, params float[] results){
  foreach(float result in results){
    Console.WriteLine($"{description}: {result}", description, result);
  }
}
```

## Fields and Properties

You may use the `readonly` keyword to tell the compiler that this value can only be written to when a constructor is invoked

```csharp
public class Animal
{
  private readonly string _name;

  public Animal(string name)
  {
    _name = name;
  }
}
```

Changing a field into a property is a great way to provide some programming logic when the value is set or get to prevent unexpected input

*Note: the value cannot be readonly anymore because it must be able to be accessed*

*Note: convention dictates that properties are to start with an uppercase letter*

```csharp
public class Animal
{
  public string Name
  {
    get {
      return _name;
    }set{
      if(!String.IsNullOrEmpty(value)){
        _name = value;
      }
    }
  }
}
```

## Events

Events are a way for a program to respond to certain notifications, the responders are called **subscribers**
