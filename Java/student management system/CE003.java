import java.util.Scanner;

/**
 *  The mark for CE003 is based on a coursework, the average of 4 homeworks, and an
 * exam, weighed as 40% for the coursework and 60% for the exam
 */
public class CE003 extends Module{

    final private float WEIGHT_EXAM = 0.6f;
    final private float WEIGHT_COURSEWORK = 0.4f;
    private int[] hwMarks = null;
    private int examMark;

    /**
     * constructor expexts  all the HW marks and the exam mark
     * @param hwMark1
     * @param hwMark2
     * @param hwMark3
     * @param hwMark4
     * @param examMark
     */
    public CE003(int [] hwMarks, int examMark){
        super("CE003", ModuleStatus.CW_AND_EXAM); // 2 for cw and exam

        this.hwMarks = hwMarks;
        this.examMark = examMark;
        calculateFinalMark();
    }

    public static Module createFromInputs(Scanner input){
        System.out.println("Enter marks for CE003 module");

        int[] hwMarks = new int [4];
        for (int i =0; i < 3 ; i++){
            System.out.println("Please enter next HW mark");
            int num = -1;
            while (num < 0 || num > 100){
                num = Integer.parseInt(input.nextLine());
            }

            hwMarks[i] = num;

        }

        System.out.println("Enter exam mark");
        int examMark = Integer.parseInt(input.nextLine());
        return new CE003(hwMarks, examMark);
    }


    /**
     *
     * @return the exam mark
     */
    public int getExamMark(){
        return this.examMark;
    }

    /**
     * sets the exam mark and recalculates the final score
     * @param examMark
     */
    public void setExamMark(int examMark){
        this.examMark = examMark;

        calculateFinalMark();
    }

    /**
     *
     * @return average of coursework marks
     */
    private float calculateCourseworkAverage(){
        int cwAverage = 0;
        for (int i =0; i < this.hwMarks.length; i++){
            cwAverage += (float)hwMarks[i]/ this.hwMarks.length;
        }
        return cwAverage;
    }

    /**
     * calculates and store final mark
     */
    public void calculateFinalMark(){

        float finalMark = WEIGHT_COURSEWORK * calculateCourseworkAverage() + WEIGHT_EXAM * examMark;
        setFinalMark(finalMark);
    }

    // CW Exam Final Mark
    public String getHeader(){
        return "CW Exam Final Mark";
    }

    /**
     *
     * @return module marks in string format
     */
    public String getMarks(){
       StringBuilder sb = new StringBuilder();
       float cw= calculateCourseworkAverage();
       sb.append(String.format("%5.2f", cw));
       //sb.append("  ");
       sb.append(String.format("%5d", examMark));
       //sb.append("  ");
       sb.append(String.format("%5.2f",getFinalMark()));

       return sb.toString();
    }
}
