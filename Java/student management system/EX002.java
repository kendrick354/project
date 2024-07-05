import java.util.Scanner;

/**
 * Module that has only exam
 */
public class EX002 extends Module {
    private int examMark;

    /**
     * constructor
     * @param examMark
     */
    public EX002(int examMark){
        super ("EX002", ModuleStatus.EXAM_ONLY); //  exam only

        this.examMark = examMark;
        setFinalMark(examMark);
    }

    public static Module createFromInputs(Scanner input){
        System.out.println("Enter marks for EX002 module");

        System.out.println("Enter exam mark");
        int examMark = Integer.parseInt(input.nextLine());
        return new EX002(examMark);
    }

    // CW Exam Final Mark
    public String getHeader(){
        return "Final Mark";
    }

    /**
     *
     * @return marks in the string format
     */
    public String getMarks(){
        StringBuilder sb = new StringBuilder();
        sb.append(getFinalMark());

        return sb.toString();
    }
}
