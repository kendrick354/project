import java.sql.SQLOutput;
import java.util.Scanner;

/**
 * Class Student: to store information about a student: ID, First name. Surname, and
 * three modules as described in the scenario
 */
public class Student {
    final private int id;
    final private String firstName;
    final private String lastName;

    Module [] modules = null;

    public Student(int id, String firstName,String lastName){
        this.id =id;
        this.firstName = firstName;
        this.lastName = lastName;

    }

    public static Student createFromInputs(Scanner input, int id){
        System.out.println("Please enter first name");
        String fn = input.nextLine();

        System.out.println("Please enter last name");
        String ln = input.nextLine();

        return new Student(id,fn, ln);
    }

    public int getID(){
        return this.id;
    }

    public String getFirstName(){
        return this.firstName;
    }

    public String getSurname(){
        return this.lastName;
    }

    public Module[] getModules(){
        return this.modules;
    }

    public Module getModule(String module){
        for (int i =0; i < this.modules.length;i++) {
            if (modules[i].getName().toLowerCase().equals(module.toLowerCase())) {
                return modules[i];
            }
        }
        return null;
    }
    public void setModules(Module[] modules){
        this.modules = modules;
    }
    public void printModuleMarks(String moduleName){
       Module module = getModule(moduleName);
       if (module != null)
       {
            System.out.print(firstName + "  " + lastName + "  " );
             System.out.println(module.getMarks());
       }

    }

    public void printAllModuleMarks(){
        if (this.modules == null) return;

        // Name Surname CW001 EX002 CE003
        System.out.printf("%10s ", this.firstName);
        //System.out.print("  ");
        System.out.printf("%9s ", this.lastName);
        //System.out.print("  ");

        for (int i = 0; i < modules.length; i++){
            System.out.print(String.format("%5.2f", modules[i].getFinalMark()));
            System.out.print("  ");
        }
        System.out.println("");
    }
}
