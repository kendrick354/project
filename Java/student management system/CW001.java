import java.util.Scanner;

/**
 * The mark for CW001 is based only on the coursework, which consist of 3 homeworks
 * and a final project; the marks are weighed as 50% for homeworks (average mark) and
 * 50% for the project.
 */
public class CW001 extends Module{

    private static float WEIGHT_HOMEWORKS = 0.5f;
    private static float WEIGHT_PROJECT = 0.5f;
    private int[] hwMarks;
    private int projectMark;

    public CW001(int[] hwMarks, int projectMark){
        super("CW001",ModuleStatus.CW_ONLY); // 0 for coursework only
        this.hwMarks = hwMarks;
        this.projectMark = projectMark;

        this.calculateFinalMark();
    }

    public static Module createFromInputs(Scanner input){
        System.out.println("Enter marks for CW001 module");

        int[] hwMarks = new int [3];
        for (int i =0; i < 3 ; i++){
            System.out.println("Please enter next HW mark");
            hwMarks[i] = Integer.parseInt(input.nextLine());
        }

        System.out.println("Enter project mark");
        int projMark = Integer.parseInt(input.nextLine());
        return new CW001(hwMarks, projMark);
    }

    /**
     *
     * @return project mark
     */
    public int getProjectMark(){
        return this.projectMark;
    }

    /**
     * sets project mark and recalculates the final
     * @param mark
     */
    public void setProjectMark(int mark){
        this.projectMark = projectMark;
        calculateFinalMark();
    }

    /**
     *
     * @return average of homowork grades
     */
    private float calculateHomeworkAverage(){
        float hmAverage = 0;
        for (int i = 0; i < this.hwMarks.length; i++){
            hmAverage += (float)this.hwMarks[i]/ this.hwMarks.length;
        }
        return hmAverage;
    }
    /**
        cacluates the final mark
     */
    public void calculateFinalMark(){
        float finalMark = WEIGHT_HOMEWORKS * calculateHomeworkAverage() + WEIGHT_PROJECT * projectMark;
        this.setFinalMark(finalMark);
    }

    // HWs Project Final Mark
    public String getHeader(){
        return "HWs Project Final Mark";
    }

    /**
     *
     * @return marks in string format
     */
    public String getMarks(){
        StringBuilder sb = new StringBuilder();
        sb.append(calculateHomeworkAverage());
        sb.append(" ");
        sb.append(projectMark);
        sb.append("  ");
        sb.append(getFinalMark());

        return sb.toString();
    }
}
