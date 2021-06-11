* validateset can be used for enum
* validatescript can be used for autompletion of folder name

# Classes

In attempt to keep with object orientation, Powershell has introduced the concept of classes. Class can be used to define a new type just like you could write `New-Object TypeName int`, you can write `New-Object -TypeName Bike`

```powershell
class Bike {
  [string]$manufacturer
  [string]$model
  [int]$year = 2016
}
```

If you now type `New-Object -TypeName Bike`, you'll see the above three properties available on the class. You can also create a constructor and use $this

```powershell
Bike(){
  this.model = 'sweet'
}
```

Just like any OOP design, you can create methods on your object

```powershell

[void] Pedal()
{
  $this.speed++
}
```

A big advantage of using classes in powershell is that you can create hidden variables that will only be accessible inside the class. This is similar to creating a private variable

```powershell
class Bike {
  [string]$manufacturer
  [string]$model
  hidden [int]$year = 2016
}
```

Now year is only accessible by internal methods.

## Inheritance

```powershell
class Bike {
  [string]$manufacturer
  [string]$model
  hidden [int]$year = 2016
  
  Bike($modelName){
    this.model = $modelName
  }
}
```

```
class threeSpeed : Bike{
  threeSpeed(): Bike("Sweet")
}
```

We can use this concept of inheritance but we'll need to pass the parameter's required by bike's constructor

