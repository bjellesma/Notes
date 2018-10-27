* Every type is either a reference type or value type

## Reference Types
Variables point to an address space in C#

* The following example assigns g1 and g2 to the same address space

```csharp
Gradebook g1 = new Gradebook();
Gradebook g2 = g1;

g1.Name = "Scott's grade book"
Console.WriteLine(g2.Name); //Scott's grade book
```

## Value Types

There is no reference to an address space because the value is stored directly in memory

* Value Types are much faster and smaller which is better for applications that need to hold a lot of numbers
* Generally, applications like video games are often done in C-based languages because video games typically need the speed
* Value types are immutable. Because of this, some objects will need to be reassigned after the method call. For example,

```csharp
DateTime date = new DateTime(2002, 8, 11);
date.AddDays(1);
Console.WriteLine(date); //8-11-2002 is returned because the value of the object hasn't been changed
date = date.AddDays(1);
Console.WriteLine(date); //8-12-2002 is returned because the object must be reassigned
```

## Pass by value

* the following code will fail because int is a primative type, a subset of a value type, and therefore will make a copy of the variable when passed as a parameter

```csharp

private void IncrementNumber(int number){
  number += 1;
}

int x = 46;
IncrementNumber(x);
Console.WriteLine( x == 47); //false
```

* the following code will pass because it is being passed a reference to an address that is already occupied

```csharp

private void AreNamesEqual(Gradebook book){
  book.Name = "A Gradebook";
}

Gradebook g1 = new Gradebook();
Gradebook g2 = g1;
AreNamesEqual(g2);
Console.WriteLine(g1.Name == "A Gradebook"); //true
Console.WriteLine(g2.Name == "A Gradebook"); //true
```

*If you were to instantiate a new Gradebook object in AreNamesEqual, the method would be creating a new object so tests would now fail*

```csharp

private void AreNamesEqual(Gradebook book){
  book = new Gradebook();
  book.Name = "A Gradebook";
}

Gradebook g1 = new Gradebook();
Gradebook g2 = g1;
AreNamesEqual(g2);
Console.WriteLine(g1.Name == "A Gradebook"); //false
Console.WriteLine(g2.Name == "A Gradebook"); //false
```

* You can make the above example use pass by reference so that the method `AreNamesEqual` explicity uses the Gradebook reference. You need to use the `ref` keyword on both the method call and declaration

```csharp

private void AreNamesEqual(ref Gradebook book){
  //The ref keyword tells us to use the reference passed to the method
  //we are now instantiating a new object for book2 because its reference was explicity passed to the method
  book = new Gradebook();
  book.Name = "A Gradebook";
}

Gradebook g1 = new Gradebook();
Gradebook g2 = g1;
AreNamesEqual(ref g2);
Console.WriteLine(g1.Name == "A Gradebook"); //false
Console.WriteLine(g2.Name == "A Gradebook"); //true
```

You can do similar in the `IncrementNumber` method

```csharp

private void IncrementNumber(ref int number){
  //because we are passing by reference, this change is reflected later in the program
  number += 1;
}

int x = 46;
IncrementNumber(ref x);
Console.WriteLine( x == 47); //true
```

**The above examples demonstrate that C# is a pass by value language**

## Arrays

* Arrays sizes are immutable so it is an expensive opperation to change the size of an array
* Lists are designed to hold a variable size

## Misc

* `int` and `System.Int32` are the same in C#
