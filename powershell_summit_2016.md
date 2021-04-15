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
