* a finally block can be used to execute after a try catch block, regardless of if an error was thrown or not
  * these are typically used to close resources
* a do while loop can be used when something is to be run at least once
```csharp
int i = 0;

do
{
    Console.WriteLine("Value of i: {0}", i);

    i++;

} while (i < 10);
```
* `break` is a statement that can be used to break iteration of a loop
```csharp
class BreakTest
{
    static void Main()
    {
        for (int i = 1; i <= 100; i++)
        {
            if (i == 5)
            {
                break;
            }
            Console.WriteLine(i);
        }

        // Keep the console open in debug mode.
        Console.WriteLine("Press any key to exit.");
        Console.ReadKey();
    }
}
```
* a `using` statement can be used with an unmanaged resource to properly manage and dispose of the resource
  * behind the scenes, the using statement will setup a try finally block so that the resources of properly disposed of
  * keep in mind that this is a try finally block and cannot be used to handle any exceptions
  * any exceptions will still crash the program
```csharp
using (Font font1 = new Font("Arial", 10.0f))
{
    byte charset = font1.GdiCharSet;
}
```
