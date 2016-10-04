import test
import genetic


code_generator = genetic.Code_generator()
code = code_generator.main()

make_task = test.Make_Task()
print(make_task.make_error("division_by_zero", code))
