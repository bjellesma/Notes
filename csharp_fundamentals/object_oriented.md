## The three pillars of object oriented programming

* Encapsilation

All about logically grouping code to hide complexity

* Inheritence

  * Though you may only inherit from one class, there is no limit to Inheritence chaining, that is, one class inheriting from another which inherits from another

  ```csharp
  public class A : B{

  }
  public class B : C{

  }
  ```

  * The keyword `base` is used to refer to the class that you are inheriting from

  * The `protected` keyword is used to keep members available to that class and derived classes

  ```cs
  public class GradeBook {
    protected List<float> grades;
    public ComputeStatistics(){
      return 4;
    }
  }
  public class ThrowAwayGradeBook : GradeBook {
    public GradeStatistics ComputeStatistics(){
      foreach(grade in grades){
        //work
      }
      return base.ComputeStatistics();
    }
  }
  ```

* Polymorphism
  * In the above code example, because ThrowAwayGradeBook inherits from Gradebook, we can say `Gradebook grades = new ThrowAwayGradeBook()`. This is because the datatype on right side of the assignment operator must be the same datatype as the left and ThrowAwayGradeBook is of type GradeBook. We cannot however say `ThrowAwayGradeBook grades = new GradeBook()`. This is polymorphic because we're changing variable behavior at runtime.
  * The advantage of this would if you have a list `List<Gradebook> grade_list = new list()` and you can now add both types `ThrowAwayGradeBook` and `GradeBook` to the list. You can then use the code as the following:

  ```cs
  foreach(Gradebook g in grade_list){
    g.ComputeStatistics();
  }
  ```

  The objects in the array of type `ThrowAwayGradeBook` will use `ComputeStatistics` method in the `ThrowAwayGradeBook` class while the objects of type `GradeBook` will use the `ComputeStatistics` method in the `GradeBook` class.

  * The difference between inheritance and polymorphism is that you can't have polymorphism without inheritance but you can have inheritance without using polymorphism

## Abstract Classes

An abstract class cannot be directly instantiated

```cs
public abstract class Window
{
  public virtual string Title {get;set;}

  public virtual void Draw()
  {
    //code
  }

  public abstract void Open();
}
```

Any class that inherits the above abstract class will need to provide a definition for Open()
