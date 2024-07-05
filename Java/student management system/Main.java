import java.util.Scanner;

/**
 * main class
 */
public class Main {

    private static Student[] students;

    /**
     * setup 3 students with all their marks
     */
    private static void setupStudents() {
        students = new Student[3];
        students[0] = new Student(1, "John", "Bradley");

        Module[] modules = new Module[3];
        int[] hwMarks = new int[]{1,2,3};
        modules[0] = new CW001(hwMarks, 4);
        modules[1] = new EX002(40);
        modules[2] = new CE003(hwMarks, 50);

        students[0].setModules(modules);

        students[1] = new Student(2, "Grace", "Hightower");

        modules = new Module[3];
        hwMarks = new int[]{1,2,3};
        modules[0] = new CW001(hwMarks, 14);
        modules[1] = new EX002(50);
        modules[2] = new CE003(hwMarks, 50);
        students[1].setModules(modules);

        students[2] = new Student(3, "Sophie", "Turner");

        modules = new Module[3];
        hwMarks = new int[]{1,2,3};
        modules[0] = new CW001( hwMarks, 24);
        modules[1] = new EX002(60);
        modules[2] = new CE003( hwMarks, 60);
        students[2].setModules(modules);

    }

    static public void setupStudentsFromInputs(Scanner input ){

        System.out.println("how many students?");
        int numStudents = Integer.parseInt(input.nextLine());

        students = new Student[numStudents];
        for (int i =0; i < numStudents;i++){
            students[i] = Student.createFromInputs(input, i);

            Module[] modules = new Module[3];

            modules[0] = CW001.createFromInputs(input);
            modules[1] = EX002.createFromInputs(input);
            modules[2] = CE003.createFromInputs(input);

            students[i].setModules(modules);

        }
    }
    public static void main(String[] args) {
        //setupStudents();

        Scanner input = new Scanner(System.in);

        setupStudentsFromInputs(input);

        String moduleName = "";
        while(true){
            System.out.println("Please enter a module name or all , for all modules");
            moduleName = input.nextLine().toLowerCase();
            if (moduleName.equals("all") ||
                    moduleName.equals("cw001") ||
                    moduleName.equals("ex002") ||
                    moduleName.equals("ce003")){
                break;
            }
        }

        // all modules marks to be printed
        if (moduleName.equals("all")) {
            System.out.println("Marks for all modules:");
            System.out.println("FirstName LastName CW001 EX002 CE003");
            for (int i = 0; i < students.length; i++) {
                students[i].printAllModuleMarks();
            }
        }
        // only specific module marks to be printed , for all students
        else {
            System.out.println("Marks for " + moduleName);
            System.out.println("FirstName LastName " + students[0].getModule(moduleName).getHeader());
            for (int i =0; i < students.length;i++){
                students[i].printModuleMarks(moduleName);
            }
        }

    }
}